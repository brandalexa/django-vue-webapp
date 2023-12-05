<template>
    <div class="list-group-item flex-column align-items-start">
        <div class="d-flex w-100 justify-content-between">
            <h5 :class="{'text-decoration-line-through': event.cancelled}" class="mb-1">{{ niceDate(event.date) }}</h5>
            <small v-if="!event.cancelled" class="text-muted">Capacity: {{ event.maxAttendees }}</small>
            <small v-if="event.cancelled"><em><strong>This event has been cancelled.</strong></em></small>
        </div>
        <div class="d-flex justify-content-between">
            <p :class="{'text-decoration-line-through': event.cancelled}" class="flex-grow-1">{{ event.description }}</p>
            <div class="d-flex mb-1">
                <button type="button" class="btn btn-primary me-1" data-bs-toggle="modal" :data-bs-target="`#edit-modal-${event.id}`">Edit</button>
                <button type="button" class="btn btn-danger" data-bs-toggle="modal" :data-bs-target="`#delete-modal-${event.id}`">Delete</button>
                <DeleteModal :eventId="event.id" @delete-event="deleteEvent"/>
                <EditModal :event="event" @update-event="updateEvent"/>
            </div>
        </div>
    </div>
</template>
<script>
import EditModal from "./EditModal.vue";
import DeleteModal from "./DeleteModal.vue";
export default {
    components: {
        EditModal,
        DeleteModal,
    },
    props: {
        event: {},
    },
    data() {
        return {
            showDeleteModal: false,
        };
    },
    methods: {
        updateEvent(updatedEvent) {
            this.$emit("update-event", updatedEvent);
        },
        deleteEvent(eventId) {
            this.$emit("delete-event", eventId);
        },
        niceDate(dateString) {
            const date = {
                year: "numeric",
                month: "short",
                day: "numeric",
                hour: "numeric",
                minute: "numeric",
                hour12: false,
                timeZone: "UTC",
            };
            const prettyDate = new Date(dateString).toLocaleDateString("en-GB", date);
            return prettyDate;
        },
    },
};
</script>