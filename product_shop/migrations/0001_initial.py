# Generated by Django 4.2.1 on 2023-07-11 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import product_shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ordered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
                ('marked_price', models.PositiveIntegerField()),
                ('selling_price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('warranty', models.CharField(max_length=50)),
                ('return_policy', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=product_shop.models.upload_to)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_by', models.CharField(max_length=200)),
                ('shipping_address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subtotal', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('order_status', models.CharField(choices=[('Order Receiving', 'OR'), ('Order Processing', 'OP'), ('On The Way', 'On The Way')], max_length=150)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product_shop.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('sub_total', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_shop.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_shop.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_shop.customer'),
        ),
    ]
