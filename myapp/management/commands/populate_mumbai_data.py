from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from myapp.models import CustomUser, DoctorProfile, PatientProfile
from datetime import date

class Command(BaseCommand):
    help = 'Populates the database with sample doctor and patient data from Mumbai, India'

    def handle(self, *args, **options):
        # Create sample doctors from Mumbai
        doctor1 = CustomUser.objects.create(
            username='dr_patel',
            email='dr.patel@mumbaihealthcare.com',
            password=make_password('doctor123'),
            user_type='doctor',
            phone_number='+919876543210',
            first_name='Rajesh',
            last_name='Patel',
            is_staff=True
        )
        
        doctor2 = CustomUser.objects.create(
            username='dr_desai',
            email='dr.desai@mumbaihealthcare.com',
            password=make_password('doctor123'),
            user_type='doctor',
            phone_number='+919876543211',
            first_name='Priya',
            last_name='Desai',
            is_staff=True
        )
        
        doctor3 = CustomUser.objects.create(
            username='dr_shah',
            email='dr.shah@mumbaihealthcare.com',
            password=make_password('doctor123'),
            user_type='doctor',
            phone_number='+919876543212',
            first_name='Amit',
            last_name='Shah',
            is_staff=True
        )

        # Create doctor profiles
        DoctorProfile.objects.create(
            user=doctor1,
            dob=date(1975, 5, 12),
            gender='M',
            medical_license_number='MH123456',
            specialization='Cardiology',
            years_of_experience=20,
            hospital_name='Lilavati Hospital, Mumbai',
            education='MBBS, MD (Cardiology) from Grant Medical College, Mumbai\nFellowship in Interventional Cardiology from AIIMS, Delhi',
            certifications='FSCAI, FACC, FESC',
            languages_spoken='English, Hindi, Gujarati',
            consultation_fee=1500.00,
            available_days='MON,TUE,WED,THU,FRI',
            available_hours='9:00 AM - 5:00 PM',
            bio='Dr. Rajesh Patel is a renowned cardiologist with over 20 years of experience in treating complex heart conditions. He has performed over 5000 cardiac procedures and is known for his expertise in interventional cardiology.'
        )

        DoctorProfile.objects.create(
            user=doctor2,
            dob=date(1980, 8, 23),
            gender='F',
            medical_license_number='MH789012',
            specialization='Pediatrics',
            years_of_experience=15,
            hospital_name='Kokilaben Dhirubhai Ambani Hospital, Mumbai',
            education='MBBS, MD (Pediatrics) from Topiwala National Medical College, Mumbai\nFellowship in Pediatric Critical Care from Boston Children\'s Hospital',
            certifications='FACP, FAAP',
            languages_spoken='English, Hindi, Marathi',
            consultation_fee=1200.00,
            available_days='MON,TUE,WED,THU,FRI,SAT',
            available_hours='10:00 AM - 7:00 PM',
            bio='Dr. Priya Desai is a dedicated pediatrician with a special interest in pediatric critical care. She has extensive experience in managing complex pediatric cases and is known for her compassionate approach to patient care.'
        )
        
        DoctorProfile.objects.create(
            user=doctor3,
            dob=date(1970, 3, 15),
            gender='M',
            medical_license_number='MH345678',
            specialization='Neurology',
            years_of_experience=25,
            hospital_name='Jaslok Hospital, Mumbai',
            education='MBBS, MD (Neurology) from King Edward Memorial Hospital, Mumbai\nFellowship in Neurocritical Care from Johns Hopkins Hospital',
            certifications='FAAN, FANA',
            languages_spoken='English, Hindi, Gujarati, Marathi',
            consultation_fee=2000.00,
            available_days='MON,TUE,WED,THU,FRI',
            available_hours='11:00 AM - 8:00 PM',
            bio='Dr. Amit Shah is a highly experienced neurologist specializing in neurocritical care and stroke management. He has published numerous research papers and is a regular speaker at international neurology conferences.'
        )

        # Create sample patients from Mumbai
        patient1 = CustomUser.objects.create(
            username='rahul_verma',
            email='rahul.verma@gmail.com',
            password=make_password('patient123'),
            user_type='patient',
            phone_number='+919876543213',
            first_name='Rahul',
            last_name='Verma'
        )

        patient2 = CustomUser.objects.create(
            username='priya_mehta',
            email='priya.mehta@gmail.com',
            password=make_password('patient123'),
            user_type='patient',
            phone_number='+919876543214',
            first_name='Priya',
            last_name='Mehta'
        )
        
        patient3 = CustomUser.objects.create(
            username='arjun_kapoor',
            email='arjun.kapoor@gmail.com',
            password=make_password('patient123'),
            user_type='patient',
            phone_number='+919876543215',
            first_name='Arjun',
            last_name='Kapoor'
        )
        
        patient4 = CustomUser.objects.create(
            username='neha_gupta',
            email='neha.gupta@gmail.com',
            password=make_password('patient123'),
            user_type='patient',
            phone_number='+919876543216',
            first_name='Neha',
            last_name='Gupta'
        )

        # Create patient profiles
        PatientProfile.objects.create(
            user=patient1,
            dob=date(1988, 11, 5),
            gender='M',
            blood_group='O+',
            height=175,
            weight=75,
            medical_history='Hypertension, diagnosed in 2020',
            allergies='None',
            current_medications='Amlodipine 5mg daily',
            last_checkup=date(2024, 3, 15),
            emergency_contact='Suresh Verma',
            emergency_relationship='Father',
            emergency_phone='+919876543217'
        )

        PatientProfile.objects.create(
            user=patient2,
            dob=date(1992, 4, 18),
            gender='F',
            blood_group='A+',
            height=162,
            weight=55,
            medical_history='Asthma, diagnosed in childhood',
            allergies='Dust, pollen',
            current_medications='Salbutamol inhaler as needed',
            last_checkup=date(2024, 2, 10),
            emergency_contact='Rajesh Mehta',
            emergency_relationship='Husband',
            emergency_phone='+919876543218'
        )
        
        PatientProfile.objects.create(
            user=patient3,
            dob=date(1975, 7, 22),
            gender='M',
            blood_group='B+',
            height=180,
            weight=82,
            medical_history='Type 2 Diabetes, diagnosed in 2018',
            allergies='None',
            current_medications='Metformin 500mg twice daily',
            last_checkup=date(2024, 1, 20),
            emergency_contact='Riya Kapoor',
            emergency_relationship='Wife',
            emergency_phone='+919876543219'
        )
        
        PatientProfile.objects.create(
            user=patient4,
            dob=date(1995, 9, 30),
            gender='F',
            blood_group='AB+',
            height=168,
            weight=58,
            medical_history='Migraine, occasional episodes',
            allergies='None',
            current_medications='Sumatriptan as needed',
            last_checkup=date(2024, 3, 5),
            emergency_contact='Vikram Gupta',
            emergency_relationship='Brother',
            emergency_phone='+919876543220'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data from Mumbai')) 