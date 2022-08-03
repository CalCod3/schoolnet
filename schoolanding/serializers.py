from rest_framework import serializers
from .models import Contact

from django.core.mail import send_mail

class ContactSerializer(serializers.ModelSerializer):
    
    
    class Meta():
        model = Contact
        fields = '__all__'
        
    def create(self, validated_data):
        contact = Contact.objects.get(id=self.id)
        subject='Thank you, {contact.first_name}, for talking to us'
        message= 'We appreciate you reaching out. Our representatives will get right on your query, so you can expect their feedback in a few days. Once more, thank you for choosing us.\nRegards,\nSchoolnet Team.\n\n Sent automatically from schoolnet.co.ke'
        email_from = settings.EMAIL_HOST_USER
        recepient_list = [contact.email,]
        send_mail(
            subject,
            message,
            email_from,
            recepient_list,
            fail_silently=False,
        )
        return instance


    
