from django.shortcuts import render
import joblib


def home(request):
    template = 'index.html'
    return render(request, template)


def result(request):
    gen_ml = joblib.load('GenesisDeploy.sav')

    lists = []
    lists.append(request.GET['credit_policy'])
    lists.append(request.GET['int_rate'])
    lists.append(request.GET['installment'])
    lists.append(request.GET['log_annual_inc'])
    lists.append(request.GET['dti'])
    lists.append(request.GET['fico'])
    lists.append(request.GET['days_with_cr'])
    lists.append(request.GET['revol_bal'])
    lists.append(request.GET['revol_util'])
    lists.append(request.GET['inq_last_6mth'])
    lists.append(request.GET['delinq2yrs'])
    lists.append(request.GET['pub_rec'])
    lists.append(request.GET['purpose_credit_card'])
    lists.append(request.GET['purpose_debt_consolidation'])
    lists.append(request.GET['purpose_educational'])
    lists.append(request.GET['purpose_home_improvement'])
    lists.append(request.GET['purpose_major_pur'])
    lists.append(request.GET['purpose_small_biz'])

    val = gen_ml.predict([lists])

    context = {'val': val, 'lists': lists}
    return render(request, 'results.html', context)
