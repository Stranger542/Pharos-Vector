export function isValidURL(str) {
  try {
    new URL(str);
    return true;
  } catch {
    return false;
  }
}
