// Problem: https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem
// Camel Case is a naming style common in many programming languages. In Java, method and variable names typically
// start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread).
// Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).
// Your task is to write a program that creates or splits Camel Case variable, method, and class names.

export function camelCase(word) {
  let [operation, typeValue, value] = word.split(";");

  if (operation == "S") {
    const allMatch = value.match(/[A-Z]/g);

    allMatch.forEach((match) => {
      value = value.replace(match, ` ${match.toLowerCase()}`);
    });

    return value.replace("()", "").trim();
  } else {
    const allMatch = value.match(/\s\w/g);

    allMatch.forEach((match) => {
      value = value.replace(match, match.trim().toUpperCase());
    });

    if (typeValue == "V") {
      return value;
    } else if (typeValue == "M") {
      return value + "()";
    } else {
      return value.replace(value[0], value[0].toUpperCase());
    }
  }
}
