from django.shortcuts import render, redirect, HttpResponse
import mysql.connector
from django.db import connection
from .forms import PaUpdateForm
from mysql.connector import Error

def home(request):
    return render(request,'home.html')

##############################################################

def researcher(request):
    return render(request,'researcher.html')

def researcher_list(request):
    return render(request,'researcher_list.html')

def addresearcher(request):
    if "POST" == request.method:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="CyRen@mysql4.85",
            database="ali"
        )

        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        Ncode = request.POST.get("Ncode")
        Birth = request.POST.get("Birth")
        Side =  request.POST.get("Side")
        tel = request.POST.get("tel")
        Email = request.POST.get("Email")
        proficiency = request.POST.get("proficiency")
        city = request.POST.get("city")
        street = request.POST.get("street")
        plaque = request.POST.get("plaque")
        IDin = request.POST.get("IDin")
        
        cursor = conn.cursor()
        out_result = cursor.callproc("add_researcher", (Ncode, IDin, Side, FirstName, LastName,  Birth,  tel, Email, proficiency, city, street, plaque, None))
        
        # out_result_value = out_result[-1]
        # print(out_result_value)
        conn.commit()
        cursor.close()
        conn.close()
        return render(request, 'home.html')

def showResearcher(request):
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="CyRen@mysql4.85",
            database="ali"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM researcher inner join personality on researcher.Ncode = personality.Ncode")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    context = {'Researcher_user': results}
    return render(request, 'researcher_list.html', context)      

def delete_researcher_view(ID_re):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CyRen@mysql4.85",
        database="ali"
    )
    cursor = conn.cursor()

    out_result = ""

    out_result = cursor.callproc('delete_researcher', args=[ID_re, out_result])
    out_result_value = out_result[-1]
    print(out_result_value)

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('researcher list')

###########################################################################################

def superrisor(request):
    return render(request,'superrisor.html')

def superrisor_list(request):
    return render(request,'superrisor_list.html')

def addsuperrisor(request):
    if "POST" == request.method:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="CyRen@mysql4.85",
            database="ali"
        )

        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        Ncode = request.POST.get("Ncode")
        Birth = request.POST.get("Birth")
        tel = request.POST.get("tel")
        Email = request.POST.get("Email")
        proficiency = request.POST.get("proficiency")
        city = request.POST.get("city")
        street = request.POST.get("street")
        plaque = request.POST.get("plaque")
        IDin = request.POST.get("IDin")

        
        cursor = conn.cursor()
        out_result = cursor.callproc("add_superrisor", (Ncode, IDin, FirstName, LastName,  Birth,  tel, Email, proficiency, city, street, plaque, None))
        
        # out_result_value = out_result[-1]
        # print(out_result_value)
        conn.commit()
        cursor.close()
        conn.close()
        return render(request, 'home.html')

def showsuperrisor(request):
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="CyRen@mysql4.85",
            database="ali"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM superrisor inner join personality on researcher.Ncode = personality.Ncode")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    context = {'superrisor_user': results}
    return render(request, 'superrisor_list.html', context)

def delete_superrisor_view(ID_su):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CyRen@mysql4.85",
        database="ali"
    )
    cursor = conn.cursor()

    out_result = ""

    out_result = cursor.callproc('delete_superrisor', args=[ID_su, out_result])
    out_result_value = out_result[-1]
    print(out_result_value)

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('researcher list')

#############################################################################################

def institute(request):
    return render(request,'institute.html')

def institute_list(request):
    return render(request,'institute_list.html')

def addinstitute(request):
    if "POST" == request.method:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="CyRen@mysql4.85",
            database="ali"
        )

        college = request.POST.get("college")
        Date_of_Establishment = request.POST.get("Date_of_Establishment")
        country = request.POST.get("country")
        city = request.POST.get("city")
        street = request.POST.get("street")
        
        cursor = conn.cursor()
        out_result = cursor.callproc("add_institute", (college, Date_of_Establishment,  country,  city, street, None))
        
        # out_result_value = out_result[-1]
        # print(out_result_value)
        conn.commit()
        cursor.close()
        conn.close()
        return render(request, 'home.html')
    
    
    
    
    
    
    
    
    
    
    
def edit_superrisor_view(request, ID_re):
    
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'CyRen@mysql4.85',
        'database': 'ali',
    }

    connection = None  # Initialize the connection variable outside the try block
    try:
        # Create a MySQL connection
        connection = mysql.connector.connect(**db_config)

        # Check if the connection is successful
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for named columns

            cursor.execute(
                "SELECT * FROM researcher inner join personality on researcher.Ncode = personality.Ncode where IDre = %s;",
                (ID_re,)
            )
            row = cursor.fetchone()
            
            if row is None:
                return render(request, 'researcher_not_found_template.html')
 
            researcher_insttance = {
                'IDre': row['IDre'],
                'Ncode': row['Ncode'],
                'Side': row['Side'],
                'fname': row['fname'],
                'lname': row['lname'],
                'dateofbirth': row['dateofbirth'],
                'tel': row['tel'],
                'email': row['email'],
                'proficiency': row['proficiency'],
                'city': row['city'],
                'street': row['street'],
                'plaque': row['plaque'],
            }

            if request.method == 'POST':
                form = PaUpdateForm(request.POST)
                form_data = form.data.dict()  # Access the raw form data as a dictionary
                form_data['IDre'] = researcher_insttance['IDre']
                form_data['Ncode'] = researcher_insttance['Ncode']



                try:
                    form = PaUpdateForm(form_data)  # Create a new form instance with updated data


                    if form.is_valid():
                        researcher_insttance.update(form.cleaned_data)

                        update_researcher_query = (
                            "UPDATE researcher SET Side = %(Side)s WHERE IDre = %(IDre)s;")
                        cursor.execute(update_researcher_query, researcher_insttance)
                        
                        update_personality_query = (
                            "UPDATE personality SET fname = %(fname)s, lname = %(lname)s, dateofbirth = %(dateofbirth)s,"
                            "tel = %(tel)s, email = %(email)s, proficiency = %(proficiency)s, city = %(city)s, street = %(street)s,"
                            "plaque = %(plaque)s WHERE Ncode = %(Ncode)s;")
                        cursor.execute(update_personality_query, researcher_insttance)
                        
                        
                        connection.commit()

                        return redirect('researcher list')
                    else:
                        print(form.errors)
                except Error as e:
                    print(f"Error: {e}")
    
            else:
                form = PaUpdateForm(initial=researcher_insttance)

            return render(request, 'researcher_update.html', {'form': form, 'researcher': researcher_insttance, 'IDre': researcher_insttance['IDre']})

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    return HttpResponse("An error occurred.")          



    
    #-----------------------------------------------



def essey(request):
    return render(request,'essey.html')

def inventions(request):
    return render(request,'inventions.html')

def budget(request):
    return render(request,'budget.html')





def essey_list(request):
    return render(request,'essey_list.html')

def inventions_list(request):
    return render(request,'inventions_list.html')

def budget_list(request):
    return render(request,'budget_list.html')

def personality_list(request):
    return render(request,'personality_list.html')

def activity_list(request):
    return render(request,'activity_list.html')


def edit_researcher_view(request, ID_re):
    
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'CyRen@mysql4.85',
        'database': 'ali',
    }

    connection = None  # Initialize the connection variable outside the try block
    try:
        # Create a MySQL connection
        connection = mysql.connector.connect(**db_config)

        # Check if the connection is successful
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for named columns

            cursor.execute(
                "SELECT * FROM researcher inner join personality on researcher.Ncode = personality.Ncode where IDre = %s;",
                (ID_re,)
            )
            row = cursor.fetchone()
            
            if row is None:
                return render(request, 'researcher_not_found_template.html')
 
            researcher_insttance = {
                'IDre': row['IDre'],
                'Ncode': row['Ncode'],
                'Side': row['Side'],
                'fname': row['fname'],
                'lname': row['lname'],
                'dateofbirth': row['dateofbirth'],
                'tel': row['tel'],
                'email': row['email'],
                'proficiency': row['proficiency'],
                'city': row['city'],
                'street': row['street'],
                'plaque': row['plaque'],
            }

            if request.method == 'POST':
                form = PaUpdateForm(request.POST)
                form_data = form.data.dict()  # Access the raw form data as a dictionary
                form_data['IDre'] = researcher_insttance['IDre']
                form_data['Ncode'] = researcher_insttance['Ncode']



                try:
                    form = PaUpdateForm(form_data)  # Create a new form instance with updated data


                    if form.is_valid():
                        researcher_insttance.update(form.cleaned_data)

                        update_researcher_query = (
                            "UPDATE researcher SET Side = %(Side)s WHERE IDre = %(IDre)s;")
                        cursor.execute(update_researcher_query, researcher_insttance)
                        
                        update_personality_query = (
                            "UPDATE personality SET fname = %(fname)s, lname = %(lname)s, dateofbirth = %(dateofbirth)s,"
                            "tel = %(tel)s, email = %(email)s, proficiency = %(proficiency)s, city = %(city)s, street = %(street)s,"
                            "plaque = %(plaque)s WHERE Ncode = %(Ncode)s;")
                        cursor.execute(update_personality_query, researcher_insttance)
                        
                        
                        connection.commit()

                        return redirect('researcher list')
                    else:
                        print(form.errors)
                except Error as e:
                    print(f"Error: {e}")
    
            else:
                form = PaUpdateForm(initial=researcher_insttance)

            return render(request, 'researcher_update.html', {'form': form, 'researcher': researcher_insttance, 'IDre': researcher_insttance['IDre']})

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    return HttpResponse("An error occurred.")     