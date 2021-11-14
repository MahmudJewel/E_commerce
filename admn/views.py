from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from customer import models as CMODEL
from customer import forms as CFORM

from admn import models as AMODEL
from admn import forms as AFORM	
# Create your views here.

def dashboard_view(request):
	context={
    'total_customer':CMODEL.Customer.objects.all().count(),
    'total_product':AMODEL.product.objects.all().count(),
    'total_categories':AMODEL.product_category.objects.all().count(),
    'total_orders':CMODEL.order.objects.all().count(),
    }
	return render(request, 'admn/admin_dashboard.html', context)

#======================= Start Admin-Customer ===============================
def admin_customer_side_var(request):
	context={
		'total_customer':CMODEL.Customer.objects.all().count(),
	}
	return render(request, 'admn/admin-customer-side.html',context)



def customer_list_view(request):
	customers=CMODEL.Customer.objects.all()
	context={
		'customers': customers
	}
	return render(request, 'admn/customer-list.html',context)


def update_customer_view(request, pk):
	#user=CMODEL.User.objects.get(id=pk)
	customer=CMODEL.Customer.objects.get(id=pk)
	user=CMODEL.User.objects.get(id=customer.user_id)
	#print('user is: ', user)
	#print('password: ', user.first_name, user.password)
	userForm = CFORM.EditForm(instance=user)
	customerForm = CFORM.customerForm(instance=customer)
	if request.method == 'POST':
		userForm = CFORM.EditForm(request.POST, instance=user)
		customerForm = CFORM.customerForm(request.POST,request.FILES, instance=customer)
		if userForm.is_valid() and customerForm.is_valid() :
			userForm.save()
			user.save()
			customerForm.save()
			return redirect('customer-list')
	context={
		'userForm' : userForm,
		'customerForm': customerForm,
		'customer':customer,
		'user' : user,
	}
	return render(request, 'admn/update-customer.html',context)



def delete_customer_view(request,  pk):
	customer = CMODEL.Customer.objects.get(id=pk)
	print(f" customer's name : {customer.mobile}")
	context = {
		"customer" : customer,
	}
	if request.method == 'POST':
		customer=CMODEL.Customer.objects.get(id=pk)
		user=CMODEL.User.objects.get(id=customer.user_id)
		user.delete()
		return redirect('customer-list')
		
	return render(request, 'admn/delete-customer.html', context)
#======================= End Admin-Customer ===============================


#======================= Start Admin-Product ===============================
def admin_product_side_var(request):
	total_product=AMODEL.product.objects.all().count()
	context={
		'total_product': total_product,
	}
	return render(request, "admn/admin-product-side.html", context)

def add_product_view(request):
	productForm=AFORM.productForm()
	if request.method=='POST':
		productForm=AFORM.productForm(request.POST , request.FILES)
		if productForm.is_valid():
			productForm.save()
			return redirect("admin-product")
	context={
		'productForm':productForm,
	}
	return render(request, "admn/add-product.html",context)

def product_list_view(request):
	products=AMODEL.product.objects.all()
	context={
		'products': products
	}
	return render(request, 'admn/product-list.html',context)

def update_product_view(request, pk):
	product=AMODEL.product.objects.get(id=pk)
	productForm=AFORM.productForm(instance=product)
	if request.method== 'POST':
		productForm=AFORM.productForm(request.POST, request.FILES, instance=product)
		if productForm.is_valid():
			productForm.save()
			return redirect('product-list')
	context={
		'productForm' : productForm
	}
	return render(request, "admn/update-product.html", context)

def delete_product_view(request, pk):
	product=AMODEL.product.objects.get(id=pk)
	if request.method=='POST':
		product=AMODEL.product.objects.get(id=pk)
		product.delete()
		return redirect('product-list')
	context={
			'product':product,
	}
	return render(request, 'admn/delete-confirm.html', context)
#======================= End Admin-Product ===============================


#======================= Start Category ===============================
def category_side_var_view(request):
	total_category = AMODEL.product_category.objects.all().count()
	context = {
		'total_category':total_category,
	}
	return render(request, 'admn/product_category.html', context)

def category_list_view(request):
	categories = AMODEL.product_category.objects.all()
	context = {
		'categories' : categories,
	}
	return render(request, 'admn/category-list.html', context)

def add_category_view(request):
	categoryForm=AFORM.categoryForm()
	if request.method == 'POST':
		categoryForm = AFORM.categoryForm(request.POST, request.FILES)
		if categoryForm.is_valid():
			categoryForm.save()
			return redirect('product-category')
	context={
		'categoryForm':categoryForm,
	}
	return render(request, 'admn/add-category.html', context)

def update_category_view(request, pk):
	category=AMODEL.product_category.objects.get(id=pk)
	categoryForm=AFORM.categoryForm(instance=category)
	if request.method== 'POST':
		categoryForm=AFORM.categoryForm(request.POST, request.FILES, instance=category)
		if categoryForm.is_valid():
			categoryForm.save()
			return redirect('category-list')
	context={
		'categoryForm' : categoryForm,
	}
	return render(request, "admn/update-category.html", context)

def delete_category_view(request, pk):
	category=AMODEL.product_category.objects.get(id=pk)
	if request.method=='POST':
		category=AMODEL.product_category.objects.get(id=pk)
		category.delete()
		return redirect('category-list')
	context={
			'category':category,
	}
	return render(request, 'admn/delete-confirm.html', context)
#======================= End Category ===============================