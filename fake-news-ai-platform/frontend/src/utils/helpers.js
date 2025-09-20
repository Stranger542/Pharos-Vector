export function truncateText(text, length = 100) {
  if (text.length <= length) return text;
  return text.slice(0, length) + "...";
}
