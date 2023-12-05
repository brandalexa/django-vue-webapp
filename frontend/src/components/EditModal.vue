<template>
    <div class="modal fade" :id="modalId" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Edit Event</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <label>Description:</label>
                <input type="text" class="form-control mb-3" v-model="modifiedEvent.description" />

                <label>Date:</label>
                <input type="text" placeholder="dd/mm/yyyy, hh:mm" class="form-control mb-3" v-model="formattedDate" />

                
                <label>Maximum attendees:</label>
                <input type="text" class="form-control mb-3" v-model="modifiedEvent.maxAttendees" />

                <div class="form-check">
                    <label class="form-check-label" :for="checkboxId">Cancelled</label>
                    <input type="checkbox" class="form-check-input mb-2" :id="checkboxId" v-model="modifiedEvent.cancelled" />
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancel</button>
                <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="updateEvent">Update</button>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        event: {},
    },
    data() {
        return {
            modifiedEvent: JSON.parse(JSON.stringify(this.event)),
            formattedDate: "",
        };
    },
    mounted() {
        this.formattedDate = this.niceDate(this.modifiedEvent.date);
    },
    computed: {
        modalId() {
            return `edit-modal-${this.event.id}`;
        },
        checkboxId() {
            return `checkbox-${this.event.id}`;
        },
    },
    methods: {
        updateEvent() {
            console.log(`Event: ${this.event.date}`);
            console.log(`Modified: ${this.modifiedEvent.date}`);
            this.$emit("update-event", this.modifiedEvent);
        },
        niceDate(unformattedDate) {
            const date = {
                year: "numeric",
                month: "2-digit",
                day: "2-digit",
                hour: "numeric",
                minute: "numeric",
                hour12: false,
                timeZone: "UTC",
            };

            const prettyDate = new Date(unformattedDate).toLocaleDateString("en-GB", date);
            return prettyDate;
        },
        toISODate(formattedDate) {
            // console.log(formattedDate);
            if (formattedDate === "") {
                return "";
            }
            const [day, month, year, time] = formattedDate.split(/[/,\s]+/);
            // console.log(day, month, year, time);
            const date = `${year}-${month}-${day}T${time}:00Z`;
            // console.log(date);
            return date;
        },
    },
    watch: {
        formattedDate(newDate) {
            this.modifiedEvent.date = this.toISODate(newDate);
        },
    },
};
</script>