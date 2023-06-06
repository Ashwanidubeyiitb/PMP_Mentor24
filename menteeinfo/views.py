from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .models import Registration
from django.core.exceptions import ValidationError
import csv
from rest_framework.decorators import api_view

# # from .resources import MentorResource
# # from django.contrib import messages
# # from tablib import Dataset

# # to upload excel file

# # def simple_upload(request):
# # 	if(request.method == 'POST'):
# # 		mentor_resource = MentorResource()
# # 		dataset = Dataset()
# # 		new_mentor = request.FILES['myfile']

# # 		if not new_mentor.name.endswith('xlsx'):
# # 			messages.info(request, 'wrong format')
# # 			return render(request, 'upload.html')
# # 		imported_data = dataset.load(new_mentor.read(), format = 'xlsx')
# # 		for data in imported_data:
# # 			value=Mentor(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
# # 			value.save()
# # 	return render(request, 'upload.html')


# # Create your views here.
# def index(request):
# 	return render(request, 'menteeinfo/index.html')

# # Mentee registration
# def register(request):
# 	corementors = Mentor.objects.filter(field="Core")
# 	Corementors = Mentor.objects.filter(field="core")
# 	consultmentors = Mentor.objects.filter(field="Consultancy")
# 	Consultmentors = Mentor.objects.filter(field="consultancy")
# 	consulting = Mentor.objects.filter(field="consulting")
# 	analyticmentors = Mentor.objects.filter(field="Analytics")
# 	finmentors = Mentor.objects.filter(field="Finance")
# 	finance = Mentor.objects.filter(field="finance")
# 	csmentor = Mentor.objects.filter(field="IT/Software")
# 	othermentors = Mentor.objects.filter(field="Other")
# 	Othermentors = Mentor.objects.filter(field="Other")
# 	Othersmentors = Mentor.objects.filter(field="Others")
# 	chutiya = Mentor.objects.filter(field="FMCG(product management")
# 	fmcg = Mentor.objects.filter(field="FMCG")
# 	bhadwa = Mentor.objects.filter(field="Analytics,")
# 	randi = Mentor.objects.filter(field="IT/Software,")
# 	corecontrol = Mentor.objects.filter(field="Mechanical(core control)")
# 	itsoftwar = Mentor.objects.filter(field="IT/Softwar")
# 	# allmentors_sorted = allmentors.order_by['gray_out']
# 	context = {
# 		'mentors_list_core': corementors, 
# 		'mentors_list_consult': consultmentors,
# 		'mentors_list_analysis': analyticmentors,
# 		'mentors_list_fin': finmentors,
# 		'mentors_list_cs': csmentor,
# 		'mentors_list_other': othermentors,
# 		'mentors_list_fmcg': fmcg,
# 		'mentors_list_Core': Corementors,
# 		'mentors_list_Other': Othermentors,
# 		'mentors_list_Others': Othersmentors,
# 		'mentors_list_chutiya': chutiya,
# 		'bhadwa': bhadwa,
# 		'randi': randi,
# 		'corecontrol': corecontrol,
# 		'Consultmentors' : Consultmentors,
# 		'consulting': consulting,
# 		'finance': finance,
# 		'itsoftwar': itsoftwar

# 	}
# 	# dict=[]
# 	# allmentors = Mentor.objects.all()
# 	# for mentor in allmentors:
		
# 	# 	exp = mentor.experience
# 	# 	explist = exp.split(",")
# 	# 	dict[mentor.rollno] = explist
# 	# print (dict[183020060])
# 	return render(request, "menteeinfo/register.html", context)
# # def mentorexp(request):
# #     allmentors = Mentor.objects.all()
# # 	for mentor in allmentors:
# #     	exp = mentor.experience


# def menteereg(request):
# 	if request.method == 'POST':
# 		# full_name = request.POST.get('full_name')
# 		roll_no = request.POST.get('roll_no')
# 		department = request.POST.get('department')
# 		degree = request.POST.get('degree')
# 		degree_other= request.POST.get('degree_other')
# 		contact_number = request.POST.get('contact')
# 		email_id = request.POST.get('email_id')
# 		preference_1 = request.POST.get('preference_1')
# 		preference_2 = request.POST.get('preference_2')
# 		preference_3 = request.POST.get('preference_3')
# 		preference_4 = request.POST.get('preference_4')
# 		preference_5 = request.POST.get('preference_5')
# 		full_name = request.POST.get('full_name')
# 		suggestion = request.POST.get('suggestion')	

# 		SOP = request.POST.get('SOP')
# 		mentee = Mentee(full_name = full_name, roll_no = roll_no,
# 			department = department, degree = degree, degree_other= degree_other,
# 			contact_number = contact_number, email_id = email_id,
# 			preference_1 = preference_1, preference_2 = preference_2,
# 			preference_3 = preference_3, preference_4 = preference_4, 
# 			preference_5 = preference_5, suggestion = suggestion, SOP = SOP)
# 		mentee.save()
# 		context = {}
# 	return render(request, 'menteeinfo/register_success.html', context)


def export(request):
	response = HttpResponse(content_type = 'text/csv')
	writer = csv.writer(response)
	writer.writerow(['fullname', 'rollno', 'department', 'other_department', 'degree', 'degree_other', 'graduation_year', 'designation', 
    'experience', 'contact', 'email', 'profiles', 'pref1', 'pref2', 'core', 'aerospace', 'chemical', 'bsbe', 'earthscience', 'ep',
    'civil','mems','maths','ieor','chemistry','electrical', 'energy','mechanical','other_mentorship', 'no_of_mentees',
    'referral', 'suggestions'])
	for registration in Registration.objects.all().values_list('fullname', 'rollno', 'department', 'other_department', 'degree', 'degree_other', 'graduation_year', 'designation', 
    'experience', 'contact', 'email', 'profiles', 'pref1', 'pref2', 'core', 'aerospace', 'chemical', 'bsbe', 'earthscience', 'ep',
    'civil','mems','maths','ieor','chemistry','electrical', 'energy','mechanical','other_mentorship', 'no_of_mentees',
    'referral', 'suggestions'):
		writer.writerow(registration)
	
	response['Content-Disposition'] = 'attachment; filename="mentors_pmp23.csv"'
	return response

def index(request):
    return render(request, 'menteeinfo/home.html')

def phonehome(request):
    return render(request, 'menteeinfo/phonehome.html')

def savedata_new(request):

    def __str__(self):
        return self.fullname

    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        rollno=request.POST.get('rollno')
        department=request.POST.get('department')
        degree=request.POST.get('degree')
        degree_other=request.POST.get('degree_other')
        graduation_year=request.POST.get('graduation_year')
        designation=request.POST.get('designation')
        experience=request.POST.get('experience')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
       
        profiles=request.POST.get('profiles')
        pref1=request.POST.get('pref1')
        pref2=request.POST.get('pref2')
        core=request.POST.get('core')
        aerospace = request.POST.get('aerospace')
        chemical = request.POST.get('chemical')
        bsbe = request.POST.get('bsbe')
        earthscience = request.POST.get('earthscience')
        ep = request.POST.get('EP')
        mems = request.POST.get('mems')
        maths = request.POST.get('maths')
        ieor = request.POST.get('ieor')
        civil = request.POST.get('civil')
        chemistry = request.POST.get('chemistry')
        electrical = request.POST.get('electrical')
        energy = request.POST.get('energy')
        mechanical = request.POST.get('mechanical')
        other_mentorship=request.POST.get('other_mentorship')
        other_department = request.POST.get('other_department')
        no_of_mentees=request.POST.get('no_of_mentees')
        referral=request.POST.get('referral')
        suggestions=request.POST.get('suggestion')

        registration=Registration(fullname=fullname, rollno=rollno, department=department, degree=degree, degree_other=degree_other, graduation_year=graduation_year, designation=designation, experience=experience, contact=contact,  email=email, profiles=profiles, pref1=pref1, pref2=pref2, core=core,
        aerospace=aerospace,
        chemical = chemical,
        bsbe = bsbe,
        earthscience = earthscience,
        ep=ep,
        mems = mems,
        maths=maths,
        ieor=ieor,
        civil=civil,
        chemistry = chemistry,
        electrical=electrical,
        energy=energy,
        mechanical=mechanical,
        other_mentorship=other_mentorship ,
        other_department = other_department,
        no_of_mentees=no_of_mentees, referral=referral,  suggestions=suggestions)
        registration.save()
        return redirect('thanks')
    return render(request, 'menteeinfo/form.html')

def thank(request):
    return render(request, 'menteeinfo/thank.html')

@api_view(['POST'])
def testapi(request):
    req_data = request.data
    alumni_id = req_data['id']
    duration = req_data['duration']
    context = {'alumni_id': alumni_id, 'duration': duration}
    return render(request, 'thank.html', context)