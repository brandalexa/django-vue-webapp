<template>
    <div class="modal fade" id="new-modal" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">New Event</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <label>Description:</label>
                <input type="text" class="form-control mb-3" v-model="event.description" />

                <label>Date:</label>
                <input type="text" placeholder="dd/mm/yyyy, hh:mm" class="form-control mb-3" v-model="formattedDate" />

                
                <label>Maximum attendees:</label>
                <input type="text" class="form-control mb-3" v-model="event.maxAttendees" />
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancel</button>
                <button type="button" class="btn btn-success" data-bs-dismiss="modal" @click="createEvent">Create</button>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            event: {
                "description": "",
                "date": "",
                "maxAttendees": "",
            },
            formattedDate: "",
        };
    },
    mounted() {
        this.formattedDate = this.niceDate(this.event.date);
    },
    methods: {
        createEvent() {
            console.log(this.event);
            this.$emit("create-event", this.event);
            this.event = {};
            this.formattedDate = "";
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
            if (prettyDate == "Invalid Date") {
                return "";
            }
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
            this.event.date = this.toISODate(newDate);
        },
    },
};
</script>