import { describe, expect, it } from "vitest";

import { camelCase } from "./camelCase4";

describe("Camel Case 4", () => {
  it.each([
    { word: "S;M;plasticCup()", expected: "plastic cup" },
    { word: "C;V;mobile phone", expected: "mobilePhone" },
    { word: "C;C;coffee machine", expected: "CoffeeMachine" },
    { word: "S;C;LargeSoftwareBook", expected: "large software book" },
    { word: "C;M;white sheet of paper", expected: "whiteSheetOfPaper()" },
    { word: "S;V;pictureFrame", expected: "picture frame" },
    { word: "S;V;iPad", expected: "i pad" },
    { word: "C;M;mouse pad", expected: "mousePad()" },
    { word: "C;C;code swarm", expected: "CodeSwarm" },
    { word: "S;C;OrangeHighlighter", expected: "orange highlighter" },
  ])(
    "should be able to create or split camel case variable, method and class names",
    ({ word, expected }) => {
      expect(camelCase(word)).toEqual(expected);
    }
  );
});
