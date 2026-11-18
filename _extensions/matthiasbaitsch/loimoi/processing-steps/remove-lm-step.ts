import { QmdDocument } from "../qmd-document.ts";
import { removeLmStep } from "../utilities.ts";
import { ProcessingStep } from "./processing-step.ts";

export class RemoveLmStep implements ProcessingStep {
  run(doc: QmdDocument): QmdDocument {
    return QmdDocument.parse(removeLmStep(doc.text()));
  }
}
