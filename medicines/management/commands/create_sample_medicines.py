from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from medicines.models import Medicine


class Command(BaseCommand):
    help = 'Create sample medicines with tablets for demo purposes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='demo',
            help='Username to create medicines for (default: demo)'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='demo123',
            help='Password for the demo user (default: demo123)'
        )

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        
        # Get or create the specified user
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': f'{username}@example.com',
                'first_name': username.title(),
                'last_name': 'User',
                'is_active': True,
            }
        )
        
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'Created user "{username}" with password: {password}')
            )
        else:
            self.stdout.write(f'Using existing user: {username}')
        
        # Sample medicines data
        sample_medicines = [
            {'name': 'Paracetamol', 'dosage': '500mg', 'quantity': 50},
            {'name': 'Ibuprofen', 'dosage': '400mg', 'quantity': 30},
            {'name': 'Aspirin', 'dosage': '300mg', 'quantity': 45},
            {'name': 'Amoxicillin', 'dosage': '250mg', 'quantity': 20},
            {'name': 'Cetirizine', 'dosage': '10mg', 'quantity': 60},
            {'name': 'Vitamin D3', 'dosage': '1000 IU', 'quantity': 90},
            {'name': 'Vitamin C', 'dosage': '500mg', 'quantity': 100},
            {'name': 'Omega-3', 'dosage': '1000mg', 'quantity': 60},
            {'name': 'Lisinopril', 'dosage': '10mg', 'quantity': 30},
            {'name': 'Metformin', 'dosage': '500mg', 'quantity': 60},
            {'name': 'Atorvastatin', 'dosage': '20mg', 'quantity': 30},
            {'name': 'Omeprazole', 'dosage': '20mg', 'quantity': 14},
            {'name': 'Loratadine', 'dosage': '10mg', 'quantity': 30},
            {'name': 'Azithromycin', 'dosage': '500mg', 'quantity': 6},
            {'name': 'Naproxen', 'dosage': '250mg', 'quantity': 20},
        ]
        
        created_count = 0
        for med_data in sample_medicines:
            medicine, created = Medicine.objects.get_or_create(
                user=user,
                name=med_data['name'],
                defaults={
                    'dosage': med_data['dosage'],
                    'quantity': med_data['quantity']
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    f'Created: {medicine.name} ({medicine.dosage}) - {medicine.quantity} tablets'
                )
            else:
                self.stdout.write(
                    f'Already exists: {medicine.name}'
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} sample medicines for user "{username}".'
            )
        )
        
        if created_count > 0:
            self.stdout.write(
                self.style.WARNING(
                    f'You can now login with username: {username} and password: {password}'
                )
            )