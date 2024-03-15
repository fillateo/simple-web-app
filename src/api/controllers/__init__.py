from .email import blueprint as email_blueprint


def setup_blueprints(app) -> None:
    app.register_blueprint(email_blueprint)
    return app


__all__ = ["setup_blueprints"]
