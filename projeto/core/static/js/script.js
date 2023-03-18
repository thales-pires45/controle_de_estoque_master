// Get the alert message element
const alertMessage = document.querySelector('.alert');

// If the alert message element exists, set a timeout to hide it after 3 seconds
if (alertMessage) {
  setTimeout(() => {
    alertMessage.style.display = 'none';
  }, 3000);
}

// Get the registration form element
const registrationForm = document.querySelector('form');

// If the registration form element exists, add an event listener to it
if (registrationForm) {
  registrationForm.addEventListener('submit', (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get the form data
    const formData = new FormData(registrationForm);

    // Send a POST request to the server with the form data
    fetch('{% url "usuarios:valida_cadastro" %}', {
      method: 'POST',
      body: formData
    })
      .then(response => {
        // If the response status is 200-299, redirect the user to the login page
        if (response.ok) {
          window.location.href = '{% url "usuarios:login" %}';
        } else {
          // Otherwise, display the error message from the server
          response.text().then(message => {
            alert(message);
          });
        }
      })
      .catch(error => {
        // Display the error message if the server request fails
        alert(error.message);
      });
  });
}
