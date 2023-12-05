"""This file contains all methods for API responses."""
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import Event


def get_all_events(request):
    """Return all events as a JSON response for API."""
    events = Event.objects.all()
    events_json = []
    for event in events:
        event_dictionary = {
            "id": event.id,
            "description": event.description,
            "date": event.date,
            "cancelled": event.cancelled,
            "maxAttendees": event.max_attendees
        }
        events_json.append(event_dictionary)

    return JsonResponse({"events": events_json})


def get_event(request, event_id):
    """Return a single event (using ID from URL) as a JSON response."""
    try:
        event = Event.objects.get(id=event_id)
        event_json = {
            "id": event.id,
            "description": event.description,
            "date": event.date,
            "cancelled": event.cancelled,
            "maxAttendees": event.max_attendees
        }

        return JsonResponse({"event": event_json}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Event does not exist."}, status=404)


@csrf_exempt
def create_event(request):
    """Create a new event based on JSON request using POST."""
    if request.method == "POST":
        try:
            request_body = json.loads(request.body.decode("utf-8"))
            description = request_body.get("description")
            date = request_body.get("date")
            max_attendees = request_body.get("maxAttendees")
            cancelled = request_body.get("cancelled")

            if cancelled is None:
                cancelled = False

            if (description or date or max_attendees) is None:
                return JsonResponse({
                    "error": "description, date, and maxAttendees cannot be null."
                    }, status=400)

            new_event = Event(
                description=description,
                date=date,
                cancelled=cancelled,
                max_attendees=max_attendees
                )
            new_event.save()
            return JsonResponse({
                "message": "Event created successfully."
                }, status=201)
        except Exception:
            return JsonResponse({
                "error": "Could not create. Invaid data provided."
                }, status=400)
    else:
        return JsonResponse({"error": "Method must be POST."}, status=405)


@csrf_exempt
def edit_event(request):
    """Modify a specified event from JSON request using PUT."""
    if request.method == "PUT":
        try:
            request_body = json.loads(request.body.decode("utf-8"))

            try:
                event = Event.objects.get(id=request_body.get("id"))
            except ObjectDoesNotExist:
                return JsonResponse({
                    "error": "Event could not be found."
                    }, status=404)

            # Conditionally update event fields
            if "description" in request_body:
                event.description = request_body.get("description")

            if "date" in request_body:
                event.date = request_body.get("date")

            if "cancelled" in request_body:
                event.cancelled = request_body.get("cancelled")

            if "maxAttendees" in request_body:
                event.max_attendees = request_body.get("maxAttendees")

            event.save()

            return JsonResponse({
                "message": "Event updated successfully."
                }, status=200)
        except Exception:
            return JsonResponse({
                "error": "Could not update. Invalid data provided."
                }, status=400)
    else:
        return JsonResponse({
            "error": "Method must be PUT."
            }, status=405)


@csrf_exempt
def delete_event(request):
    """Delete a specified event from JSON request using DELETE."""
    if request.method == "DELETE":
        try:
            request_body = json.loads(request.body.decode("utf-8"))

            try:
                event = Event.objects.get(id=request_body.get("id"))
            except ObjectDoesNotExist:
                return JsonResponse({
                    "error": "Event could not be found."
                    }, status=404)

            event.delete()

            return JsonResponse({
                "message": "Event deleted successfully."
                }, status=200)
        except Exception:
            return JsonResponse({
                "error": "Could not delete. Invalid data provided."
                }, status=400)
    else:
        return JsonResponse({
            "error": "Method must be DELETE."
            }, status=405)
