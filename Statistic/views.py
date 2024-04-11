from django.shortcuts import render, redirect
from Auth.models import User

# Create your views here.
def statistic_index(request):
  if not request.user.is_authenticated:
    return redirect("home")
  
  last_connections = User.objects.all().order_by('-last_login')

  xp_stats = User.objects.all().order_by('xp')

  context={"last_connections": last_connections, "xp_stats": xp_stats}
  return render(request, "statistic_index.html", context=context)