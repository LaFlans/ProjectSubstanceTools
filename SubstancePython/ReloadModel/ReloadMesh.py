import os
import substance_painter.project

def start_plugin():
    print("ReloadMeshStart")
    reload_mesh()

def close_plugin():
    print("ReloadMeshClose")
    reload_mesh()

# メッシュリロード
def reload_mesh():
    if not substance_painter.project.is_open():
        substance_painter.logging.log(
            substance_painter.logging.ERROR,
            "ReloadMesh",
            "プロジェクトが開かれていません")
        return

    # メッシュパス取得
    mesh_path = substance_painter.project.last_imported_mesh_path()
    if not os.path.exists(mesh_path):
        substance_painter.logging.log(
            substance_painter.logging.ERROR,
            "ReloadMesh",
            "最後にimportしたメッシュファイルが存在しません")
        return

    # メッシュリロード設定
    mesh_reload_settings = substance_painter.project.MeshReloadingSettings(
        import_cameras=True,
        preserve_strokes=True)

    substance_painter.project.reload_mesh(
        mesh_path,
        mesh_reload_settings,
        on_mesh_reload)

# メッシュのリロード成功時に呼び出す関数
def on_mesh_reload(status: substance_painter.project.ReloadMeshStatus):
    if status == substance_painter.project.ReloadMeshStatus.SUCCESS:
        print("メッシュのリロードが完了しました")
    else:
        print("メッシュのリロードに失敗しました") 
