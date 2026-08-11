from pathlib import Path

def read_project_context(project_path, max_files=10):
    project = Path(project_path)
    context = []

    extensions = [".js", ".ts", ".tsx", ".py", ".json"]

    count = 0

    for file in project.rglob("*"):
        if file.suffix in extensions and count < max_files:
            try:
                content = file.read_text(encoding="utf-8")[:3000]

                context.append(
                    f"FILE: {file.relative_to(project)}\n{content}"
                )

                count += 1

            except:
                pass

    return "\n\n".join(context)