from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from myapp.models import CustomUser, DoctorProfile, PatientProfile
from datetime import date

class Command(BaseCommand):
    help = 'Populates the database with sample doctor and patient data'

    def handle(self, *args, **options):
        # Create sample doctors
        doctor1 = CustomUser.objects.create(
            username='dr_smith',
            email='dr.smith@example.com',
            password=make_password('doctor123'),
            user_type='doctor',
            phone_number='+1234567890',
            is_staff=True
        )
        
        doctor2 = CustomUser.objects.create(
            username='dr_jones',
            email='dr.jones@example.com',
            password=make_password('doctor123'),
            user_type='doctor',
            phone_number='+1987654321',
            is_staff=True
        )

        # Create doctor profiles
        DoctorProfile.objects.create(
            user=doctor1,
            dob=date(1980, 1, 1),
            gender='M',
            medical_license_number='MD123456',
            specialization='Cardiology',
            years_of_experience=15,
            hospital_name='City General Hospital'
        )

        DoctorProfile.objects.create(
            user=doctor2,
            dob=date(1975, 6, 15),
            gender='F',
            medical_license_number='MD789012',
            specialization='Pediatrics',
            years_of_experience=20,
            hospital_name='Children\'s Hospital'
        )

        # Create sample patients
        patient1 = CustomUser.objects.create(
            username='john_doe',
            email='john.doe@example.com',
            password=make_password('patient123'),
            user_type='patient',
            phone_number='+1122334455'
        )

        patient2 = CustomUser.objects.create(
            username='jane_smith',
            email='jane.smith@example.com',
            password=make_password('patient123'),
            user_type='patient',
            phone_number='+5566778899'
        )

        # Create patient profiles
        PatientProfile.objects.create(
            user=patient1,
            dob=date(1990, 3, 15),
            gender='M',
            blood_group='O+',
            height=175,
            weight=70,
            medical_history='No significant medical history'
        )

        PatientProfile.objects.create(
            user=patient2,
            dob=date(1985, 8, 22),
            gender='F',
            blood_group='A+',
            height=165,
            weight=55,
            medical_history='Allergic to penicillin'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data')) 