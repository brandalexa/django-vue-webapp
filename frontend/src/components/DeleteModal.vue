<template>
    <div class="modal fade" :id="modalId" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Warning</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p>Once deleted, events cannot be recovered - consider setting this event as cancelled.</p>
                    <p><strong>Are you sure you want to delete this event?</strong></p>
                    <small class="text-muted">Event ID: {{ eventId }}</small>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Cancel</button>
                    <button @click="deleteEvent" type="button" class="btn btn-danger" data-bs-dismiss="modal">Delete</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        eventId: Number,
    },
    computed: {
        modalId() {
            return `delete-modal-${this.eventId}`;
        },
    },
    methods: {
        deleteEvent() {
            this.$emit("delete-event", this.eventId);
        },
    },
};
</script>