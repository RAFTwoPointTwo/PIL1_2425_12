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

    toggleVehiculeSection();

    roleField.addEventListener("change", toggleVehiculeSection);
});
</script>
