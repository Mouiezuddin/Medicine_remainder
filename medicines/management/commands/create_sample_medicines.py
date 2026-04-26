from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from medicines.models import Medicine


class Command(BaseCommand):
    help = 'Create sample medicines with 50 tablets each'

    def handle(self, *args, **options):
        # Get or create a user (you can modify this to use a specific user)
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(f'Created admin user with password: admin123')
        
        # Sample medicines data
        sample_medicines = [
            {'name': 'Paracetamol', 'dosage': '500mg', 'quantity': 50},
            {'name': 'Ibuprofen', 'dosage': '200mg', 'quantity': 50},
            {'name': 'Aspirin', 'dosage': '100mg', 'quantity': 50},
            {'name': 'Vitamin D3', 'dosage': '1000 IU', 'quantity': 50},
            {'name': 'Omega-3', 'dosage': '1000mg', 'quantity': 50},
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
                f'Successfully created {created_count} sample medicines with 50 tablets each.'
            )
        )