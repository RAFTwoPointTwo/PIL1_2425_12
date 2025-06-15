<script>
document.addEventListener("DOMContentLoaded", function() {
    const roleField = document.getElementById("id_role");
    const vehiculeSection = document.getElementById("vehicule-section");

    function toggleVehiculeSection() {
        if (roleField.value === "Conducteur") {
            vehiculeSection.style.display = "block";
        } else {
            vehiculeSection.style.display = "none";
        }
    }

    // Initialisation au chargement
    toggleVehiculeSection();

    // Réagir aux changements
    roleField.addEventListener("change", toggleVehiculeSection);
});
</script>
