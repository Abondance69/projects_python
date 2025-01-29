class FlightApp {
    async getData() {
      try {
        // URL de l'API que tu souhaites appeler
        const apiUrl = 'https://api.example.com/flights'; // Remplace cette URL par celle de ton API
  
        // Faire un appel API avec fetch
        const response = await fetch(apiUrl);
  
        if (!response.ok) {
          throw new Error(`Erreur HTTP: ${response.status}`);
        }
  
        // Convertir la réponse en format JSON
        const data = await response.json();
  
        // Traiter les données récupérées
        console.log('Données récupérées:', data);
        return data;
      } catch (error) {
        // Gestion des erreurs
        console.error('Erreur lors de l\'appel API:', error);
      }
    }
  }
  
  // Exemple d'utilisation de la classe
  const app = new FlightApp();
  app.getData();
  