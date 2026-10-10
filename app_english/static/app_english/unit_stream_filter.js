document.addEventListener("DOMContentLoaded", () => {
  const levelField = document.getElementById("id_level");
  const streamField = document.getElementById("id_stream");

  if (!levelField || !streamField) return;

  const filterStreams = () => {
    const level = levelField.value;

    for (const option of streamField.options) {
      if (!option.value) continue;

      const matches = !level || option.dataset.level === level;
      option.hidden = !matches;
      option.disabled = !matches;

      if (!matches && option.selected) streamField.value = "";
    }
  };

  levelField.addEventListener("change", filterStreams);
  filterStreams();
});
