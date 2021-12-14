from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from pandas import period_range
import json

from .models import Candidate


# Create your views here.


def TotalExperienceCounter(workExperiences):
    periods = []
    monthsOfExperience = set()
    try:
        for period in workExperiences:
            periods.append([dates for dates in period.values()])
        periods = sorted(periods)
        for period in periods:
            for month in period_range(period[0], period[1], freq="M").strftime("%Y %b"):
                monthsOfExperience.add(month)
        yearsOfExperience = len(monthsOfExperience) // 12
        return yearsOfExperience
    except:
        return "Error"


def candidates(request):

    if request.method == "GET":
        candidatesJson = []

        for candidate in Candidate.objects.all():
            candidateInfo = {
                "id": candidate.id,
                "name": candidate.name,
                "totalExperience": candidate.totalExperience,
                "workExperience": candidate.workExperience,
            }
            candidatesJson.append(candidateInfo)

        return JsonResponse(
            {
                "candidates": sorted(
                    candidatesJson, key=lambda i: i["totalExperience"], reverse=True
                )
            }
        )

    elif request.method == "POST":
        data = json.loads(request.body)
        warning = "Incorrect data! Provide name and dates in format: Mon Year"

        if data:

            if (
                not (data["name"] and data["workExperience"])
                or TotalExperienceCounter(data["workExperience"]) == "Error"
            ):
                return HttpResponseBadRequest(warning)

            name = data["name"]
            workExperience = data["workExperience"]
            totalExperience = TotalExperienceCounter(data["workExperience"])

            candidate = Candidate.objects.create(
                name=name,
                totalExperience=totalExperience,
                workExperience=workExperience,
            )
            candidate.save()
            return HttpResponse("THANK YOU! Data saved")

        else:
            return HttpResponseBadRequest("Empty package")
