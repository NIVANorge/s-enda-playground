from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class SchemaComponentType:
    """A schema component includes a schema fragment (type definition) or an
    entire schema from some target namespace; the schema language is identified
    by URI.

    If the component is a schema fragment its parent MUST be referenced
    (parentSchema).
    """
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetNamespace",
            "type": "Attribute",
            "required": True,
        }
    )
    parent_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentSchema",
            "type": "Attribute",
        }
    )
    schema_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLanguage",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
