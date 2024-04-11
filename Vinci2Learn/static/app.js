const goToLogin = () => {
  window.location.href = "/auth/login";
};

const goToLessons = () => {
  window.location.href = "/lesson/all";
};

const goToLesson = (id) => {
  window.location.href = `/lesson/${id}`;
};

const getReward = (id) => {
  window.location.href = `/lesson/reward/${id}`;
};

const xp_max = (value) => {
  document.getElementById("xp_max").innerHTML = value * 100;
};

const reward = (value, lessonXp, level) => {
  const xp_reward = document.getElementById("xp_reward");
  const level_reward = document.getElementById("level_reward");

  if (xp_reward) {
    xp_reward.innerHTML = `${value - lessonXp} -> ${value} xp`;
  }

  if (level_reward) {
    level_reward.innerHTML = `Level: ${level - 1} -> ${level}`;
  }
};
