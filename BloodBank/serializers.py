from rest_framework import serializers
from .models import Donor

class DonorSerializer(serializers.ModelSerializer):
    RFID = serializers.CharField(max_length=30)

    class Meta:
        model = Donor
        fields = ['RFID']

    def create(self, validated_data):
        rfid_value = validated_data.pop('RFID')
        # You can process the RFID value here before saving it
        donor = Donor.objects.create(RFID=rfid_value)
        return donor