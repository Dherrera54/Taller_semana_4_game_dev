

import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_enemy_hunter_state import CEnemyHunterState
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_special import CTagSpecial
from src.create.prefab_creator import create_explosion


def system_collision_enemy_special(world: esper.World, explosion_info: dict):
    components_enemy = world.get_components(CSurface, CTransform, CTagEnemy)
    components_special = world.get_components(CSurface, CTransform, CTagSpecial)

    for enemy_entity, (c_s, c_t, c_ene) in components_enemy:
        ene_rect = c_s.area.copy()
        ene_rect.topleft = c_t.pos
        for special_entity, (c_s_s, c_s_t, c_spec) in components_special:
            special_rect = c_s_s.area.copy()
            special_rect.topleft = c_s_t.pos
            if ene_rect.colliderect(special_rect) and c_spec.special_type!="mine":
                world.delete_entity(enemy_entity)
                world.delete_entity(special_entity)
                create_explosion(world, c_t.pos, explosion_info)