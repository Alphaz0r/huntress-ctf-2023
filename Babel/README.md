# Babel
## It's babel! Just a bunch of gibberish, right?

A file is included with the challenge

---

It's a obfuscated C# file.

The very end is intersting because we can use the code to deobfuscate itself without doing it manually

```c#
string YKyumnAOcgLjvK = "lQwSYRxgfBHqNucMsVonkpaTiteDhbXzLPyEWImKAdjZFCOvJGrU";
Assembly smlpjtpFegEH = Assembly.Load(Convert.FromBase64String(zcfZIEShfvKnnsZ(pTIxJTjYJE, YKyumnAOcgLjvK)));
MethodInfo nxLTRAWINyst = smlpjtpFegEH.EntryPoint;
nxLTRAWINyst.Invoke(smlpjtpFegEH.CreateInstance(nxLTRAWINyst.Name), null);
}}}
```

Commenting the last lines and modifying the third one with a `Console.WriteLine` helped me get the output clean. 


```c#
string YKyumnAOcgLjvK = "lQwSYRxgfBHqNucMsVonkpaTiteDhbXzLPyEWImKAdjZFCOvJGrU";
Console.WriteLine(pTIxJTjYJE, YKyumnAOcgLjvK);
//MethodInfo nxLTRAWINyst = smlpjtpFegEH.EntryPoint;
//nxLTRAWINyst.Invoke(smlpjtpFegEH.CreateInstance(nxLTRAWINyst.Name), null);
}}}
```

I remember erasing the Base64 conversion so I decoded it myself, gaving me an executable.

Running `strings` on it gave me the flag :)