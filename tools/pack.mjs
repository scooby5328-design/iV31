import { createPackage } from "@electron/asar";

const [src, dest] = process.argv.slice(2);
if (!src || !dest) {
  console.error("usage: node tools/pack.mjs <folder> <resources.neu>");
  process.exit(1);
}
await createPackage(src, dest);
