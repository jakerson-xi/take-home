// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

document.getElementById("myForm").addEventListener("submit", function (event) {
    const decimalInput = document.getElementById("id_total_amount");
    const decimalValue = decimalInput.value;
  
    // Regular expression to validate decimal number with a dot
    const regex = /^\d+(\.\d{1,2})?$/;
  
    if (!regex.test(decimalValue)) {
      // Display a Bootstrap error message
      swal("ERROR", "Please enter a valid decimal number with up to 2 decimal places.", "error");
      decimalInput.value = ""
      // Add the is-invalid class to the input field
      decimalInput.classList.add("is-invalid");
  
      event.preventDefault(); // Prevent form submission
    } else {
      // If the validation passes, remove the is-invalid class
      decimalInput.classList.remove("is-invalid");
    }
  });





