function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }
  
    window.addEventListener("load", function() {
        document.getElementById("submitButton").addEventListener("keydown", function(event) {
            // Check if the pressed key is the space key (keyCode 32 or key " ")
            if (event.keyCode === 32 || event.key === " ") {
                // Prevent the default space key behavior (e.g., scrolling the page)
                event.preventDefault();
                // Submit the form
                document.getElementById("uploadForm").submit();
            }
        });
    })

  