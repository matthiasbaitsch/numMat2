# Input, use functions to be able to have input on top
SOURCE_CONTENT() = [
    "bausteine/_templates/pyproject.toml" => keep_name,
    "bausteine/_templates/uv.lock" => keep_name,
    "bausteine/_templates/projekt.code-workspace" => workspace_name
]

TARGET_ROOTS() = ["bausteine", "lernpfad/veranstaltung"]

# Transform names
function workspace_name(path, _)
    if startswith(path, "lernpfad")
        return basename(path) * ".code-workspace"
    end
    # e.g. bausteine/01-grundlagen/aufgaben/projekt -> aufgaben-grundlagen
    m = match(r"bausteine/\d\d-([\w-]+)/(\w+)/", path)
    s = replace(basename(path), r"^projekt" => "")
    return m[2] * "-" * m[1] * s * ".code-workspace"
end

keep_name(_, source) = basename(source)

# Do the work, run from the project root
cd(joinpath(@__DIR__, ".."))

for bd = TARGET_ROOTS(), (path, dirs, files) = walkdir(bd)
    # Parked building blocks (bausteine/_geparkt) are not delivered and get no templates
    if endswith(path, r"projekt|projekt\-[\w-]+") && !occursin("/_geparkt/", path)
        for (source, transform) = SOURCE_CONTENT()
            target = joinpath(path, transform(path, source))
            println(target)
            cp(source, target, force=true)
        end
    end
end

# Python environment for executed {python} cells in the project root, used by make with uv run (not checked in)
for f = ("pyproject.toml", "uv.lock")
    println(f)
    cp(joinpath("bausteine/_templates", f), f, force=true)
end
