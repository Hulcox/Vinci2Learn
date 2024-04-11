from django.contrib.auth.forms import UserCreationForm
from Auth.models import User

class CreateUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User  # Remplacez MonUtilisateurPersonnalise par votre modèle personnalisé
        fields = UserCreationForm.Meta.fields