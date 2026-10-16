import * as ResEdit from 'resedit';
import * as PE from 'pe-library';
import fs from 'fs';

const [file, ver] = process.argv.slice(2);
const exe = PE.NtExecutable.from(fs.readFileSync(file), {ignoreCert: true});
const res = PE.NtExecutableResource.from(exe);
const vi = ResEdit.Resource.VersionInfo.fromEntries(res.entries)[0];
const [a, b, c] = ver.split('.').map(Number);
vi.setFileVersion(a, b, c, 0, 1033);
vi.setProductVersion(a, b, c, 0, 1033);
vi.setStringValues({lang: 1033, codepage: 1200}, {FileVersion: ver, ProductVersion: ver});
vi.outputToResourceEntries(res.entries);
res.outputResource(exe);
fs.writeFileSync(file, Buffer.from(exe.generate()));
