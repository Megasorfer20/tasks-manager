const addTaskButton = document.getElementById("add-task");
const modal = document.getElementById("task-modal");
const closeModal = document.getElementById("close-modal");
const taskForm = document.getElementById("task-form");
const tasksContainer = document.querySelector(".tasks-container");
const filterButtons = document.querySelectorAll('.filter-buttons');

addTaskButton.addEventListener("click", () => {
  modal.classList.add("active");
});

closeModal.addEventListener("click", () => {
  modal.classList.remove("active");
});

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      filterButtons.forEach(btn => btn.classList.remove('active'));

      button.classList.add('active');
    });
  });

taskForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.getElementById("task-title").value;
  const description = document.getElementById("task-desc").value;

  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `
          <div class="status">
            <strong>Status: </strong>
            <p>Undone</p>
          </div>
          <div class="content-data">
            <h3>${title}</h3>
            <p>${description}</p>
          </div>
          <div class="buttons-task">
            <button>Delete</button>
            <button>Mark as Done</button>
          </div>
        `;

  tasksContainer.appendChild(card);
  modal.classList.remove("active");
  taskForm.reset();
});