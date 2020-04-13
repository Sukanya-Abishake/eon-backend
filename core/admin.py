from django.contrib import admin

# Register your models here.
from core.models import EventType, Event, Invitation, EventPreference, Subscription, UserProfile, WishList, Notification


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type")
    search_fields = ("type",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "type", "date", "time", "location", "subscription_fee", "no_of_tickets", "sold_tickets",
        "is_cancelled")
    search_fields = ("name", "type", "event_created_by")
    readonly_fields = ("images", "external_links", "event_created_by", "sold_tickets")


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "user", "discount_percentage", "email")
    search_fields = ("event", "user")


@admin.register(EventPreference)
class EventPreferenceAdmin(admin.ModelAdmin):
    list_display = ("id", "event_type", "user")
    search_fields = ("event_type", "user")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "user", "no_of_tickets", "payment", 'is_active')
    search_fields = ("event", "user")


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "user", "is_active")
    search_fields = ("event", "user")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "contact_number", "organization", "role")
    search_fields = ("user", "contact_number", "organization", "role")
    readonly_fields = ('user',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "event", "message", "has_read")
    search_fields = ("user", "event", "message", "has_read")
