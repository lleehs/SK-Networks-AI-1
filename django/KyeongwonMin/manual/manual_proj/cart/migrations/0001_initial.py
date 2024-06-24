# Generated by Django 4.2.13 on 2024-06-19 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_product_productimage'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cartId', models.AutoField(primary_key=True, serialize=False)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='account.account')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('cartItemId', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'cart_item',
            },
        ),
    ]
