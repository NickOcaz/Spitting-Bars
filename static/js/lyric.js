const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const isProtectedCheckbox = document.getElementById("is_protected");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      e.preventDefault(); // Prevents the default behavior of the button
      let lyricID = e.target.getAttribute("lyric_id");
      deleteConfirm.href = `/lyric_delete/${lyricID}`;
      deleteModal.show();
    });
}

// Toggle delete button visibility based on is_protected checkbox
isProtectedCheckbox.addEventListener("change", (e) => {
    for (let button of deleteButtons) {
        button.style.display = e.target.checked ? "none" : "inline-block";
    }
});

// Initial check to set the visibility on page load
document.addEventListener("DOMContentLoaded", () => {
    for (let button of deleteButtons) {
        button.style.display = isProtectedCheckbox.checked ? "none" : "inline-block";
    }
});