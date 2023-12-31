/* pb_common.c: Common support functions for pb_encode.c and pb_decode.c.
 *
 * 2014 Petteri Aimonen <jpa@kapsi.fi>
 */

#include "pb_common.h"
#include "os.h"

bool pb_field_iter_begin(pb_field_iter_t *iter, const pb_field_t *fields, void *dest_struct) {
    iter->start = (const pb_field_t *) PIC(fields);
    iter->pos = (const pb_field_t *) PIC(fields);
    iter->required_field_index = 0;
    iter->dest_struct = dest_struct;
    iter->pData = (char *) dest_struct + iter->pos->data_offset;
    iter->pSize = (char *) iter->pData + iter->pos->size_offset;

    return (iter->pos->tag != 0);
}

bool pb_field_iter_next(pb_field_iter_t *iter) {
    const pb_field_t *prev_field = ((const pb_field_t *) PIC(iter->pos));

    if (prev_field->tag == 0) {
        /* Handle empty message types, where the first field is already the terminator.
         * In other cases, the iter->pos never points to the terminator. */
        return false;
    }

    iter->pos = ((const pb_field_t *) PIC(iter->pos)) + 1;

    if (((const pb_field_t *) PIC(iter->pos))->tag == 0) {
        /* Wrapped back to beginning, reinitialize */
        (void) pb_field_iter_begin(iter,
                                   ((const pb_field_t *) PIC(iter->start)),
                                   iter->dest_struct);
        return false;
    } else {
        /* Increment the pointers based on previous field size */
        size_t prev_size = prev_field->data_size;

        if (PB_HTYPE(prev_field->type) == PB_HTYPE_ONEOF &&
            PB_HTYPE(((const pb_field_t *) PIC(iter->pos))->type) == PB_HTYPE_ONEOF &&
            ((const pb_field_t *) PIC(iter->pos))->data_offset == PB_SIZE_MAX) {
            /* Don't advance pointers inside unions */
            return true;
        } else if (PB_ATYPE(prev_field->type) == PB_ATYPE_STATIC &&
                   PB_HTYPE(prev_field->type) == PB_HTYPE_REPEATED) {
            /* In static arrays, the data_size tells the size of a single entry and
             * array_size is the number of entries */
            prev_size *= prev_field->array_size;
        } else if (PB_ATYPE(prev_field->type) == PB_ATYPE_POINTER) {
            /* Pointer fields always have a constant size in the main structure.
             * The data_size only applies to the dynamically allocated area. */
            prev_size = sizeof(void *);
        }

        if (PB_HTYPE(prev_field->type) == PB_HTYPE_REQUIRED) {
            /* Count the required fields, in order to check their presence in the
             * decoder. */
            iter->required_field_index++;
        }

        iter->pData =
            (char *) iter->pData + prev_size + ((const pb_field_t *) PIC(iter->pos))->data_offset;
        iter->pSize = (char *) iter->pData + ((const pb_field_t *) PIC(iter->pos))->size_offset;
        return true;
    }
}

bool pb_field_iter_find(pb_field_iter_t *iter, uint32_t tag) {
    const pb_field_t *start = ((const pb_field_t *) PIC(iter->pos));

    do {
        if (((const pb_field_t *) PIC(iter->pos))->tag == tag &&
            PB_LTYPE(((const pb_field_t *) PIC(iter->pos))->type) != PB_LTYPE_EXTENSION) {
            /* Found the wanted field */
            return true;
        }

        (void) pb_field_iter_next(iter);
    } while (((const pb_field_t *) PIC(iter->pos)) != start);

    /* Searched all the way back to start, and found nothing. */
    return false;
}

extern void _ebss;

// Return true if there is less than MIN_BSS_STACK_GAP bytes available in the stack
bool check_stack_overflow(uint16_t min_bss_stack_gap) {
    uint32_t stack_top = 0;

    PRINTF("+++++++Stack remaining: CUR STACK ADDR: %p, EBSS: %p, diff: %d\n",
           &stack_top,
           &_ebss,
           ((uintptr_t) &stack_top) - ((uintptr_t) &_ebss));
    if (((uintptr_t) &stack_top) < (((uintptr_t) &_ebss) + min_bss_stack_gap)) {
        return true;
    }

    return false;
}
