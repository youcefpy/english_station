document.addEventListener("DOMContentLoaded", () => {
  const levelField = document.getElementById("id_level");
  const streamField = document.getElementById("id_stream");
  const unitField = document.getElementById("id_unit");

  if (!levelField) return;

  const filterStreams = () => {
    const level = levelField.value;

    if (streamField) {
      for (const option of streamField.options) {
        if (!option.value) continue;

        const matches = !level || option.dataset.level === level;
        option.hidden = !matches;
        option.disabled = !matches;

        if (!matches && option.selected) streamField.value = "";
      }
    }

    filterUnits();
  };

  const filterUnits = () => {
    if (!unitField) return;

    const level = levelField.value;
    const stream = streamField?.value;

    for (const option of unitField.options) {
      if (!option.value) continue;

      const matchesLevel = !level || option.dataset.level === level;
      const matchesStream = !stream || option.dataset.stream === stream;
      const matches = matchesLevel && matchesStream;
      option.hidden = !matches;
      option.disabled = !matches;

      if (!matches && option.selected) unitField.value = "";
    }
  };

  levelField.addEventListener("change", filterStreams);
  streamField?.addEventListener("change", filterUnits);
  filterStreams();
});
