<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            Corporate Events
        </div>
        <div id="liveAlertPlaceholder"></div>
        <button type="button" class="btn btn-secondary mb-2" data-bs-toggle="modal" data-bs-target="#new-modal">New Event</button>
        <NewModal @create-event="createEvent"/>
        <div class="list-group"> 
            <ListEventItem v-for="event in events" :key="event.id" :event="event" @update-event="updateEvent" @delete-event="deleteEvent"/>
        </div>
    </div>
</template>
<script>
import ListEventItem from "./components/ListEventItem.vue";
import NewModal from "./components/NewModal.vue";
export default {
    components: {
    ListEventItem,
    NewModal,
},
    data() {
        return {
            events: [],
            selectedEvent: {},
            editModalVisible: false,
        }
    },
    async mounted() {
        await this.getEvents();
    },
    methods: {
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
        async createEvent(event) {
            console.log(event);
            const response = await fetch(`http://localhost:8000/api/new-event/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(event),
            });

            const responseData = await response.json();
            if (responseData.message != null) {
                this.showAlert(responseData.message, "success"); 
            }
            else {
                this.showAlert(responseData.error, "danger"); 
            }

            await this.getEvents();
            console.log(response.data);
        },
        async getEvents() {
            const response = await fetch("http://localhost:8000/api/events.json", {
                method: "GET",
            });
            const responseData = await response.json();
            this.events = responseData.events;
        },
        async updateEvent(updatedEvent) {
            console.log(updatedEvent);
            const response = await fetch(`http://localhost:8000/api/edit-event/`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(updatedEvent),
            });

            const responseData = await response.json();
            if (responseData.message != null) {
                this.showAlert(responseData.message, "success"); 
            }
            else {
                this.showAlert(responseData.error, "danger"); 
            }
            
            await this.getEvents();
        },
        async deleteEvent(id) {
            const response = await fetch("http://localhost:8000/api/delete-event/", { 
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({"id": id}),
            });

            const responseData = await response.json();
            if (responseData.message != null) {
                this.showAlert(responseData.message, "success"); 
            }
            else {
                this.showAlert(responseData.error, "danger"); 
            }
            await this.getEvents();
        },
        showAlert(message, type) {
            const alertPlaceholder = document.getElementById('liveAlertPlaceholder');
            const wrapper = document.createElement('div');
            wrapper.innerHTML = [
                `<div class="alert alert-${type} alert-dismissible" role="alert">`,
                `   <div>${message}</div>`,
                '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
                '</div>'
            ].join('');

            alertPlaceholder.append(wrapper)
        },
    },
};
</script>
<style>
li {
    display: flex;
}
</style>