
document.querySelector("#registro").addEventListener("change", (e) => {
  const inputs = document.querySelectorAll("#registro input");
  inputs.forEach((input) => {

    if (e.target === input) {
      let span = document.querySelector(`#${input.id}Span`);
      if (!span) {
        let spanVirtual = document.createElement("span");
        spanVirtual.id = `${input.id}Span`;
        spanVirtual.classList.add("error", "none");
        spanVirtual.textContent = input.title;
        span = spanVirtual;

      }

      let validation;
      switch (input.id) {
        case "username":
          validation = input.value.trim().match(/^[a-zA-Z0-9]+$/g);
          break;

        case "mail":
          validation = input.value.trim().match(/[-.\w]+@([\w-]+\.)+[\w-]+/g);

          break;

        case "repeat_mail":
          let mail = document.querySelector("#mail");
          input.value.trim() === mail.value.trim()
            ? (validation = true)
            : (validation = false);
          break;

        case "pass":
          validation = input.value.trim().match(/^(?=.+[a-z])(?=.+[A-Z])(?=.+[0-9])(?=.+[/$@!_¡?])[A-z\d/$@!_¡?].{8,15}$/g);
          break;

        case "repeat_pass":
          let pass = document.querySelector("#pass");
          input.value.trim() === pass.value.trim()
            ? (validation = true)
            : (validation = false);
          break;
      }

      if (span.textContent !== input.title) span.textContent = input.title;

      (validation === null || validation === false) &&
      (input.value !== "" || input.value.includes(" "))
        ? span.classList.remove("none")
        : span.classList.add("none");
      
      if (span.classList.value=="error"){
        span.classList.add("text-danger-emphasis")
        input.insertAdjacentElement("afterend", span);
      }else{span.remove()

      }
    }
  });
});
