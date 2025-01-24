from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def index(request):
    all_group = BloodGroup.objects.annotate(total=Count('donor'))
    return render(request, "index.html", {'all_group':all_group})

def donors_list(request, myid):
    blood_groups = BloodGroup.objects.filter(id=myid).first()
    donor = Donor.objects.filter(blood_group=blood_groups)
    return render(request, "donors_list.html", {'donor':donor})

def donors_details(request, myid):
    details = Donor.objects.filter(id=myid)[0]
    return render(request, "donors_details.html", {'details':details})

def request_blood(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        date = request.POST['date']
        blood_requests = RequestBlood.objects.create(name=name, email=email, phone=phone, state=state, city=city, address=address, blood_group=BloodGroup.objects.get(name=blood_group), date=date)
        blood_requests.save()
        return render(request, "index.html")
    return render(request, "request_blood.html")

@login_required(login_url = '/login')
def see_all_request(request):
    user_blood_group = request.user.donor.blood_group
    requests = RequestBlood.objects.filter(blood_group=user_blood_group)
    # requests = RequestBlood.objects.all()
    return render(request, "see_all_request.html", {'requests':requests})

def become_donor(request):
    error_message = None  # Initialize error message
    if request.method == "POST":
        # Get data from the form
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        date = request.POST['date']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, "become_donor.html", {"error_message": error_message})

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists."
            return render(request, "become_donor.html", {"error_message": error_message})

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            error_message = "Email already exists."
            return render(request, "become_donor.html", {"error_message": error_message})

        # Create the user
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)

        # Create the donor profile
        try:
            blood_group_instance = BloodGroup.objects.get(name=blood_group)
        except BloodGroup.DoesNotExist:
            error_message = "Invalid blood group."
            return render(request, "become_donor.html", {"error_message": error_message})

        donors = Donor.objects.create(donor=user, phone=phone, state=state, city=city, address=address, gender=gender, blood_group=blood_group_instance, date_of_birth=date, image=image)

        # Save user and donor
        user.save()
        donors.save()

        # Redirect to the index page or a success page
        return redirect("index")  # or use render(request, "index.html")
    
    return render(request, "become_donor.html", {"error_message": error_message})
def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        error_message = None  # Initialize error message
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            # Check if the username exists
            if not User.objects.filter(username=username).exists():
                error_message = "Username does not exist."
            else:
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)  # Log in the user
                    return redirect("/profile")
                else:
                    error_message = "Incorrect password."

        return render(request, "login.html", {"error_message": error_message})


def Logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url = '/login')
def profile(request):
    donor_profile = Donor.objects.get(donor=request.user)
    return render(request, "profile.html", {'donor_profile':donor_profile})

@login_required(login_url = '/login')
def edit_profile(request):
    donor_profile = Donor.objects.get(donor=request.user)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']

        donor_profile.donor.email = email
        donor_profile.phone = phone
        donor_profile.state = state
        donor_profile.city = city
        donor_profile.address = address
        donor_profile.save()
        donor_profile.donor.save()

        try:
            image = request.FILES['image']
            donor_profile.image = image
            donor_profile.save()
        except:
            pass
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html", {'donor_profile':donor_profile})

@login_required(login_url = '/login')
def change_status(request):
    donor_profile = Donor.objects.get(donor=request.user)
    if donor_profile.ready_to_donate:
        donor_profile.ready_to_donate = False
        donor_profile.save()
    else:
        donor_profile.ready_to_donate = True
        donor_profile.save()
    return redirect('/profile')