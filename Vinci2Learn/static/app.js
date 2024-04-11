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
