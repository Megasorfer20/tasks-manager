const addTaskButton = document.getElementById("add-task");
const modal = document.getElementById("task-modal");
const closeModal = document.getElementById("close-modal");
const taskForm = document.getElementById("task-form");
const tasksContainer = document.querySelector(".tasks-container");
const filterButtons = document.querySelectorAll(".filter-buttons");

const allFetchButton = document.getElementById("all-tasks");
const checkedFetchButton = document.getElementById("unchecked-tasks");
const uncheckedFetchButton = document.getElementById("checked-tasks");

// Maneja el evento cuando PyWebView está listo
document.addEventListener("pywebviewready", async () => {
  console.log("PyWebView API ready");

  try {
    await loadTasks();
  } catch (error) {
    console.error("Error loading tasks:", error);
  }
});

async function loadTasks() {
  if (!window.pywebview || !window.pywebview.api) {
    console.error("PyWebView API is not available");
    return;
  }

  try {
    const tasks = await window.pywebview.api.get_tasks();
    tasksContainer.innerHTML = ""; // Limpia las tareas anteriores
    tasks.forEach((task) => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
            <div class="status">
              <strong>Status: </strong>
              <p>${task.checked ? "Done" : "Undone"}</p>
            </div>
            <div class="content-data">
              <h3>${task.title}</h3>
              <p>${task.description}</p>
            </div>
            <div class="buttons-task">
              <button onclick="deleteTask(${task.id})">Delete</button>
              <button onclick="toggleTask(${task.id})">${
        task.checked ? "Mark as Undone" : "Mark as Done"
      }</button>
            </div>
          `;
      tasksContainer.appendChild(card);
    });
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }
}

async function loadUncheckedTasks() {
  if (!window.pywebview || !window.pywebview.api) {
    console.error("PyWebView API is not available");
    return;
  }

  try {
    const tasks = await window.pywebview.api.get_unchecked_tasks();
    tasksContainer.innerHTML = ""; // Limpia las tareas anteriores
    tasks.forEach((task) => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
          <div class="status">
            <strong>Status: </strong>
            <p>${task.checked ? "Done" : "Undone"}</p>
          </div>
          <div class="content-data">
            <h3>${task.title}</h3>
            <p>${task.description}</p>
          </div>
          <div class="buttons-task">
            <button onclick="deleteTask(${task.id})">Delete</button>
            <button onclick="toggleTask(${task.id})">${
        task.checked ? "Mark as Undone" : "Mark as Done"
      }</button>
          </div>
        `;
      tasksContainer.appendChild(card);
    });
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }
}

async function loadCheckedTasks() {
  if (!window.pywebview || !window.pywebview.api) {
    console.error("PyWebView API is not available");
    return;
  }

  try {
    const tasks = await window.pywebview.api.get_checked_tasks();
    tasksContainer.innerHTML = ""; // Limpia las tareas anteriores
    tasks.forEach((task) => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
          <div class="status">
            <strong>Status: </strong>
            <p>${task.checked ? "Done" : "Undone"}</p>
          </div>
          <div class="content-data">
            <h3>${task.title}</h3>
            <p>${task.description}</p>
          </div>
          <div class="buttons-task">
            <button onclick="deleteTask(${task.id})">Delete</button>
            <button onclick="toggleTask(${task.id})">${
        task.checked ? "Mark as Undone" : "Mark as Done"
      }</button>
          </div>
        `;
      tasksContainer.appendChild(card);
    });
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }
}

// Eventos del modal
addTaskButton.addEventListener("click", () => {
  modal.classList.add("active");
});

closeModal.addEventListener("click", () => {
  modal.classList.remove("active");
});

// Filtro de botones
filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    filterButtons.forEach((btn) => btn.classList.remove("active"));
    button.classList.add("active");

    // Actualizar tareas según el filtro seleccionado
    if (button.id === "all-tasks") {
      loadTasks();
    } else if (button.id === "unchecked-tasks") {
      loadUncheckedTasks();
    } else if (button.id === "checked-tasks") {
      loadCheckedTasks();
    }
  });
});

// Manejo del formulario de tareas
taskForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("task-title").value;
  const description = document.getElementById("task-desc").value;

  try {
    const response = await window.pywebview.api.add_task(title, description);
    console.log(response.message);

    await loadTasks();
  } catch (error) {
    console.error("Error adding task:", error);
  }

  modal.classList.remove("active");
  taskForm.reset();
});

// Función para alternar el estado de una tarea
async function toggleTask(taskId) {
  try {
    const response = await window.pywebview.api.toggle_task(taskId);
    console.log(response.message);

    await loadTasks();
  } catch (error) {
    console.error("Error toggling task:", error);
  }
}

// Función para eliminar una tarea
async function deleteTask(taskId) {
  try {
    const response = await window.pywebview.api.delete_task(taskId);
    console.log(response.message);

    await loadTasks();
  } catch (error) {
    console.error("Error deleting task:", error);
  }
}

async function exportTasks() {
  try {
    const response = await window.pywebview.api.export_tasks_to_json();

    if (response.status === "success") {
      const filename = response.filename;

      // Realiza una solicitud para obtener el archivo
      const fileResponse = await fetch(`http://localhost:8000/${filename}`);

      if (!fileResponse.ok) {
        throw new Error(`HTTP error! Status: ${fileResponse.status}`);
      }

      const blob = await fileResponse.blob();
      const url = URL.createObjectURL(blob);

      // Crear un enlace temporal y forzar la descarga
      const link = document.createElement("a");
      link.href = url;
      link.download = filename;

      document.body.appendChild(link);
      link.click(); // Simular el clic para descargar
      document.body.removeChild(link); // Limpiar el enlace temporal

      console.log("Archivo descargado exitosamente");
      alert(
        `El archivo fue exportado exitosamente en la dirección ${response.path}`
      );
    } else {
      alert("Error: " + response.message);
    }
  } catch (error) {
    console.error("Error exporting tasks:", error);
    alert("Error al exportar las tareas: " + error.message);
  }
}

// Asociar la función exportTasks al botón de exportación
document.getElementById("export-button").addEventListener("click", exportTasks);
