from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from xhtml2pdf import pisa


# Create your views here.

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def get(request):
	if request.method=='POST' and 'submit' in request.POST:
		name=request.POST['applicant_name']
		fname=request.POST['fname']
		mname=request.POST['mname']
		dob=request.POST["dob"]
		gender=request.POST['gender']
		cast=request.POST['caste']
		scast=request.POST['subcaste']
		hno=request.POST['hno']
		vil=request.POST['village']
		mandal=request.POST['mandal']
		dis=request.POST['district']
		pin=request.POST['pin']
		mobile=request.POST['mobile']
		pur=request.POST['purpose']
		ad=request.POST['aadhar']
		email=request.POST['mail']
		
		pdf = render_to_pdf('pdf.html',{'name':name,"f":fname,"m":mname,"dob":dob,"gen":gender,"c":cast,"subc":scast,"mob":mobile,"mail":email,
		"acard":ad,"p":pur,"zip":pin,"dis":dis,"mdl":mandal,"vill":vil,"hno":hno,})
		return HttpResponse(pdf, content_type='application/pdf')
	elif request.method=='POST' and 'display' in request.POST:
		name=request.POST['applicant_name']
		fname=request.POST['fname']
		mname=request.POST['mname']
		return render(request,"pdf_view.html",{'name':name,"f":fname,"m":mname})	


def index(request):
	return render(request,"index.html")    

def trial(request):
	return render(request,"trial.html")
def tri(request):
	name=request.POST['name']
	dic={
		"name":name
	}
	return render(request,"trial.html",dic)
		
	


		